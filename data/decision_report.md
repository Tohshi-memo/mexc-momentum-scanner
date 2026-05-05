# Decision Report

- generated_at: 2026-05-05T20:53:05.689558+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3384**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3384, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.18% | **-0.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +3.17% | **+0.95%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.67% | **+0.67%** |
| LIMIT_4PCT | 12/20 | 60.0% | +1.05% | **+0.63%** |
| LIMIT_2PCT | 17/20 | 85.0% | -0.02% | **-0.02%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | -0.07% | **-0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +1.96% | **+1.23%** |
| ASK_LONG | 20/20 | 100.0% | +0.61% | **+0.61%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.23% | **+0.55%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.77% | **+0.54%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.02% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T20:52:59.826375+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=81578.8
- Funnel: target 760 → liquid 189 → pre 50 → checked 50 → surge 5 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.3 >= 65=2, 4h RSI 84.8 >= 65=1, 4h RSI 84.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +38.47% | $16,736,667.12 |
| MAVIA/USDT:USDT | +24.28% | $1,050,357.06 |
| SWARMS/USDT:USDT | +20.50% | $2,237,279.56 |
| SMCISTOCK/USDT:USDT | +16.41% | $4,076,995.95 |
| ZEC/USDT:USDT | +13.67% | $497,433,261.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIN/USDT:USDT | below_1h_threshold | +4.76% | +4.73% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +4.74% | +4.71% |
| ZEN/USDT:USDT | below_1h_threshold | +4.72% | +4.69% |
| MAVIA/USDT:USDT | below_1h_threshold | +3.96% | +3.93% |
| FILECOIN/USDT:USDT | below_1h_threshold | +3.45% | +3.42% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
