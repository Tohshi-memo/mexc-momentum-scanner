# Decision Report

- generated_at: 2026-05-03T06:12:18.490119+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3041**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3041, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+0.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.17% | **+0.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 8/11 | 72.7% | +1.80% | **+1.31%** |
| LIMIT_4PCT | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.54% | **+0.38%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.91% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +2.63% | **+1.71%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.65% | **+0.83%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.84% | **+0.46%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.62% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T06:12:16.678546+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=78126.2
- Funnel: target 755 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BABY/USDT:USDT | +44.43% | $3,868,938.30 |
| BR/USDT:USDT | +27.85% | $2,458,838.47 |
| AKT/USDT:USDT | +15.97% | $1,302,729.26 |
| BSB/USDT:USDT | +14.40% | $14,310,349.32 |
| FIGHT/USDT:USDT | +11.30% | $1,016,031.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.41% | +4.51% |
| BABY/USDT:USDT | below_1h_threshold | +3.08% | +3.19% |
| LUNC/USDT:USDT | below_1h_threshold | +1.48% | +1.58% |
| MOVR/USDT:USDT | below_1h_threshold | +1.12% | +1.22% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +0.93% | +1.03% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
