# Decision Report

- generated_at: 2026-05-02T02:52:26.997325+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2852**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2852, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.92% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.13% | **+1.39%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.66% | **+1.25%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.79% | **+0.98%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +2.50% | **+0.88%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.25% | **+0.82%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 7件 (TP 4 / SL 3 / EXP 0)
- 最新: BIO/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T02:52:25.011295+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=78375.1
- Funnel: target 755 → liquid 175 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +77.80% | $30,256,865.50 |
| SKYAI/USDT:USDT | +17.19% | $22,147,383.94 |
| B/USDT:USDT | +16.10% | $68,850,198.09 |
| BLESS/USDT:USDT | +15.63% | $1,650,964.86 |
| PLAY/USDT:USDT | +8.69% | $4,435,117.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +4.86% | +4.76% |
| SKYAI/USDT:USDT | below_1h_threshold | +4.59% | +4.49% |
| TAC/USDT:USDT | below_1h_threshold | +4.58% | +4.48% |
| ORCA/USDT:USDT | below_1h_threshold | +2.25% | +2.15% |
| BR/USDT:USDT | below_1h_threshold | +1.82% | +1.72% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
