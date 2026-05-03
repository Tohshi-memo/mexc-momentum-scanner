# Decision Report

- generated_at: 2026-05-03T09:47:05.881916+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3058**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3058, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +1.83% | **+0.73%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_3PCT | 18/20 | 90.0% | +0.03% | **+0.02%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.64% | **+2.00%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.35% | **+1.84%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +3.28% | **+1.64%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.65% | **+1.24%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +2.93% | **+0.73%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T09:47:03.776051+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=78450.0
- Funnel: target 755 → liquid 166 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BABY/USDT:USDT | +52.05% | $15,743,011.88 |
| TST/USDT:USDT | +40.73% | $1,083,709.35 |
| B/USDT:USDT | +32.31% | $44,385,095.30 |
| FHE/USDT:USDT | +21.43% | $3,066,568.31 |
| TAC/USDT:USDT | +19.26% | $2,808,571.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_1h_threshold | +2.07% | +1.93% |
| THETA/USDT:USDT | below_1h_threshold | +1.85% | +1.71% |
| BSB/USDT:USDT | below_1h_threshold | +1.59% | +1.45% |
| CHILLGUY/USDT:USDT | below_1h_threshold | +1.45% | +1.31% |
| ORCA/USDT:USDT | below_1h_threshold | +1.38% | +1.24% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
