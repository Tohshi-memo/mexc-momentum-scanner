# Decision Report

- generated_at: 2026-06-06T19:36:08.948932+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5890**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5890, expectancy=-0.02%
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
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.22% | **+0.73%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 2件 (TP 0 / SL 2 / EXP 0)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$135.02** / 初期 $100.00 (+35.02%)
- 確定: 1023件 (Win 244 / Loss 314 / Flat 465) / skip 1428件
- 成長率目線: 平均log +0.000294 / 幾何平均 +0.029% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $135.02

## 4. Latest Market Context

- 更新: 2026-06-06T19:36:03.287557+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=60537.7
- Funnel: target 771 → liquid 134 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +32.73% | $45,225,776.93 |
| BTW/USDT:USDT | +30.15% | $17,573,491.79 |
| FIDA/USDT:USDT | +27.31% | $1,554,423.21 |
| SKYAI/USDT:USDT | +25.44% | $14,190,684.22 |
| BLUAI/USDT:USDT | +11.88% | $7,176,008.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.27% | +4.38% |
| SKYAI/USDT:USDT | below_1h_threshold | +4.24% | +4.35% |
| BSB/USDT:USDT | below_1h_threshold | +3.37% | +3.48% |
| AAOISTOCK/USDT:USDT | below_1h_threshold | +1.57% | +1.68% |
| BLUAI/USDT:USDT | below_1h_threshold | +1.49% | +1.60% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
