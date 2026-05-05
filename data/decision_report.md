# Decision Report

- generated_at: 2026-05-05T09:27:13.890639+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3341**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3341, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +3.17% | **+0.48%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.50% | **+0.28%** |
| LIMIT_BB3S | 2/11 | 18.2% | +1.29% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +3.00% | **+3.00%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +3.44% | **+2.93%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +4.22% | **+2.53%** |
| ASK_LONG | 20/20 | 100.0% | +1.95% | **+1.95%** |
| LIMIT_BB3S_LONG | 4/9 | 44.4% | +3.36% | **+1.49%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T09:27:11.716134+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=80625.0
- Funnel: target 765 → liquid 198 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +89.06% | $15,509,611.94 |
| LAB/USDT:USDT | +59.35% | $85,791,104.50 |
| HIVE/USDT:USDT | +34.91% | $4,211,694.27 |
| FHE/USDT:USDT | +33.78% | $4,496,315.50 |
| M/USDT:USDT | +25.62% | $6,736,345.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAVE/USDT:USDT | below_1h_threshold | +3.61% | +3.79% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.86% | +3.05% |
| PNUT/USDT:USDT | below_1h_threshold | +2.49% | +2.68% |
| TURBO/USDT:USDT | below_1h_threshold | +2.19% | +2.37% |
| PRL/USDT:USDT | below_1h_threshold | +1.42% | +1.61% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
