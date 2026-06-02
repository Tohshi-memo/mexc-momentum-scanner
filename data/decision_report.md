# Decision Report

- generated_at: 2026-06-02T18:12:02.752967+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5482**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5482, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-2.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.70% | **-2.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +4.06% | **+1.42%** |
| LIMIT_6PCT | 9/20 | 45.0% | +2.59% | **+1.17%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +6.21% | **+0.93%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.16% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +4.17% | **+3.48%** |
| MARKET_LONG | 20/20 | 100.0% | +2.58% | **+2.58%** |
| ASK_LONG | 20/20 | 100.0% | +2.54% | **+2.54%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +3.28% | **+2.30%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.92% | **+1.61%** |

## 2. $100 Live Portfolio

- 残高: **$97.10** / 初期 $100.00 (-2.90%)
- 確定トレード: 89件 (TP 26 / SL 60 / EXP 3)
- 最新: ENA/USDT:USDT SL_HIT PnL -3.88% 残高後 $97.10
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.39** / 初期 $100.00 (+30.39%)
- 確定: 976件 (Win 229 / Loss 300 / Flat 447) / skip 1067件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $130.39

## 4. Latest Market Context

- 更新: 2026-06-02T18:12:00.425076+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=67596.4
- Funnel: target 770 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +37.97% | $11,582,303.67 |
| ENA/USDT:USDT | +18.73% | $39,516,397.93 |
| LIT/USDT:USDT | +15.05% | $3,494,408.42 |
| ESPORTS/USDT:USDT | +11.06% | $11,554,016.77 |
| PIEVERSE/USDT:USDT | +10.34% | $5,323,323.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ENA/USDT:USDT | below_1h_threshold | +2.18% | +1.99% |
| EDGE/USDT:USDT | below_1h_threshold | +1.90% | +1.71% |
| AAVE/USDT:USDT | below_1h_threshold | +1.76% | +1.57% |
| BILL/USDT:USDT | below_1h_threshold | +0.69% | +0.50% |
| FET/USDT:USDT | below_1h_threshold | +0.60% | +0.41% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
