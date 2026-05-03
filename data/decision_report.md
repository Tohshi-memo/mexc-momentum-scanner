# Decision Report

- generated_at: 2026-05-03T13:37:11.321718+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3071**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3071, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.55% | **-1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 19/20 | 95.0% | +1.05% | **+1.00%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_BB3S | 11/17 | 64.7% | +0.05% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.79% | **+1.90%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +4.39% | **+1.76%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +4.00% | **+1.60%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.35% | **+1.57%** |
| LIMIT_7PCT_LONG | 4/20 | 20.0% | +3.46% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T13:37:08.813657+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=78634.4
- Funnel: target 755 → liquid 169 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.4 >= 65=1, 4h RSI 74.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +42.47% | $3,717,685.27 |
| TAC/USDT:USDT | +37.64% | $2,531,260.31 |
| NAORIS/USDT:USDT | +30.51% | $4,156,477.57 |
| AIGENSYN/USDT:USDT | +29.02% | $4,879,793.49 |
| FHE/USDT:USDT | +25.85% | $4,178,647.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +3.86% | +3.96% |
| AKT/USDT:USDT | below_1h_threshold | +3.81% | +3.92% |
| ZEN/USDT:USDT | below_1h_threshold | +2.78% | +2.88% |
| XNY/USDT:USDT | below_1h_threshold | +2.73% | +2.83% |
| FIGHT/USDT:USDT | below_1h_threshold | +2.59% | +2.70% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
