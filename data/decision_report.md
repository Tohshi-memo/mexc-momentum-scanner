# Decision Report

- generated_at: 2026-05-04T05:12:15.239611+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3154**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3154, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+0.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.14% | **+0.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/13 | 38.5% | +1.78% | **+0.68%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.71% | **+0.43%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT | 4/20 | 20.0% | +0.70% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.42% | **+0.85%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.98% | **+0.79%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.76% | **+0.42%** |
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +0.56% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T05:12:13.357096+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=80173.4
- Funnel: target 758 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +63.30% | $21,345,501.35 |
| SKYAI/USDT:USDT | +48.93% | $45,254,559.21 |
| LAB/USDT:USDT | +45.72% | $215,888,699.37 |
| TAG/USDT:USDT | +40.76% | $7,184,679.39 |
| TST/USDT:USDT | +38.92% | $6,334,336.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SIREN/USDT:USDT | below_1h_threshold | +3.56% | +3.72% |
| SAPIEN/USDT:USDT | below_1h_threshold | +2.71% | +2.87% |
| GONGJIAN/USDT:USDT | below_1h_threshold | +2.69% | +2.85% |
| MEGA/USDT:USDT | below_1h_threshold | +2.63% | +2.79% |
| TST/USDT:USDT | below_1h_threshold | +2.09% | +2.24% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
