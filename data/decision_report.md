# Decision Report

- generated_at: 2026-06-06T19:25:00.011245+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5888**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5888, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +6.33% | **+0.63%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.20% | **+1.60%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.46% | **+1.17%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.87% | **+0.94%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 2件 (TP 0 / SL 2 / EXP 0)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$134.18** / 初期 $100.00 (+34.18%)
- 確定: 1022件 (Win 243 / Loss 314 / Flat 465) / skip 1427件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $134.18

## 4. Latest Market Context

- 更新: 2026-06-06T19:24:54.775065+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=60633.0
- Funnel: target 771 → liquid 134 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +30.64% | $17,395,128.54 |
| LAB/USDT:USDT | +30.07% | $43,917,671.70 |
| FIDA/USDT:USDT | +22.26% | $1,528,863.98 |
| SKYAI/USDT:USDT | +19.70% | $13,683,528.88 |
| BLUAI/USDT:USDT | +10.07% | $7,154,052.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.00% | +3.96% |
| WLD/USDT:USDT | below_1h_threshold | +2.27% | +2.22% |
| BABY/USDT:USDT | below_1h_threshold | +1.72% | +1.67% |
| BSB/USDT:USDT | below_1h_threshold | +1.42% | +1.38% |
| LUNC/USDT:USDT | below_1h_threshold | +1.28% | +1.23% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
