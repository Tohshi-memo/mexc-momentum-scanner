# Decision Report

- generated_at: 2026-04-30T14:56:11.313007+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2711**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2711, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.04% | **-0.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.69% | **+0.66%** |
| LIMIT_BB3S | 6/18 | 33.3% | +1.68% | **+0.56%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +7.03% | **+7.03%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.50% | **+1.12%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.73% | **+1.09%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.40% | **+0.84%** |

## 2. $100 Live Portfolio

- 残高: **$100.50** / 初期 $100.00 (+0.50%)
- 確定トレード: 2件 (TP 1 / SL 1 / EXP 0)
- 最新: UB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.50
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T14:56:09.079527+00:00 / 保存件数 24/288
- BTC: STAGNANT 1h -0.04% price=76338.9
- Funnel: target 760 → liquid 228 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.1 >= 65=1, 4h RSI 79.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +41.10% | $1,924,088.01 |
| BSB/USDT:USDT | +38.99% | $44,775,173.62 |
| SKYAI/USDT:USDT | +32.85% | $23,896,504.98 |
| ROLL/USDT:USDT | +24.58% | $2,945,827.74 |
| BIO/USDT:USDT | +21.19% | $3,507,192.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIVER/USDT:USDT | below_1h_threshold | +3.50% | +3.54% |
| QCOMSTOCK/USDT:USDT | below_1h_threshold | +2.64% | +2.69% |
| PENDLE/USDT:USDT | below_1h_threshold | +2.21% | +2.25% |
| POWER/USDT:USDT | below_1h_threshold | +2.20% | +2.25% |
| RKLBSTOCK/USDT:USDT | below_1h_threshold | +2.04% | +2.08% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
