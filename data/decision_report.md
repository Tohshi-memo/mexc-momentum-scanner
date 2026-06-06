# Decision Report

- generated_at: 2026-06-06T19:30:33.780084+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5889**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5889, expectancy=-0.02%
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
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.46% | **+1.17%** |
| ASK_LONG | 20/20 | 100.0% | +0.97% | **+0.97%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.75% | **+0.87%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 2件 (TP 0 / SL 2 / EXP 0)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$135.02** / 初期 $100.00 (+35.02%)
- 確定: 1023件 (Win 244 / Loss 314 / Flat 465) / skip 1427件
- 成長率目線: 平均log +0.000294 / 幾何平均 +0.029% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $135.02

## 4. Latest Market Context

- 更新: 2026-06-06T19:30:28.227869+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=60582.0
- Funnel: target 771 → liquid 134 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +30.47% | $44,472,654.67 |
| BTW/USDT:USDT | +29.21% | $17,467,538.02 |
| SKYAI/USDT:USDT | +24.71% | $13,897,217.86 |
| FIDA/USDT:USDT | +22.26% | $1,536,078.35 |
| BLUAI/USDT:USDT | +9.41% | $7,157,205.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +3.67% | +3.70% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.64% | +3.68% |
| WLD/USDT:USDT | below_1h_threshold | +1.97% | +2.01% |
| BSB/USDT:USDT | below_1h_threshold | +1.61% | +1.65% |
| LUNC/USDT:USDT | below_1h_threshold | +1.40% | +1.44% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
