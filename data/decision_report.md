# Decision Report

- generated_at: 2026-05-04T16:22:27.976035+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3233**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3233, expectancy=-0.18%
- 直近20件 MARKET基準: n=20, expectancy=-2.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.10% | **-2.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 16/20 | 80.0% | +1.75% | **+1.40%** |
| LIMIT_6PCT | 5/20 | 25.0% | +5.55% | **+1.39%** |
| LIMIT_ATR | 13/20 | 65.0% | +2.00% | **+1.30%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.97% | **+0.89%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +5.07% | **+2.53%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.93% | **+1.76%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.75% | **+1.57%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$102.36** / 初期 $100.00 (+2.36%)
- 確定トレード: 14件 (TP 5 / SL 7 / EXP 2)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T16:22:22.420618+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.35% price=80260.6
- Funnel: target 761 → liquid 199 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.1 >= 65=1, 4h RSI 73.2 >= 65=1, 4h RSI 65.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +13.93% | $19,672,514.43 |
| BSB/USDT:USDT | +11.68% | $33,607,052.35 |
| ASTEROID/USDT:USDT | +8.00% | $5,159,172.31 |
| TAG/USDT:USDT | +5.60% | $17,565,790.28 |
| GIGA/USDT:USDT | +5.17% | $2,361,137.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGA/USDT:USDT | below_relative_strength | +5.18% | +4.82% |
| UB/USDT:USDT | below_1h_threshold | +3.57% | +3.21% |
| ELIZAOS/USDT:USDT | below_1h_threshold | +3.37% | +3.02% |
| B3/USDT:USDT | below_1h_threshold | +2.84% | +2.48% |
| GIGGLE/USDT:USDT | below_1h_threshold | +2.79% | +2.43% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
