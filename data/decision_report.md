# Decision Report

- generated_at: 2026-06-12T00:11:20.140158+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6427**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6427, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.14% | **-0.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/18 | 16.7% | +3.69% | **+0.61%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.10% | **+0.39%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.38% | **+0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.52% | **+0.68%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.20% | **+0.48%** |
| MARKET_LONG | 20/20 | 100.0% | +0.38% | **+0.38%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.72% | **+0.36%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.50% | **+0.35%** |

## 2. $100 Live Portfolio

- 残高: **$94.70** / 初期 $100.00 (-5.30%)
- 確定トレード: 15件 (TP 1 / SL 13 / EXP 1)
- 最新: XPL/USDT:USDT SL_HIT PnL -3.46% 残高後 $94.70
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.41** / 初期 $100.00 (+51.41%)
- 確定: 1327件 (Win 344 / Loss 427 / Flat 556) / skip 1661件
- 成長率目線: 平均log +0.000313 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ID/USDT:USDT `MARKET_LONG` EXPIRED account -0.04% 残高後 $151.41

## 4. Latest Market Context

- 更新: 2026-06-12T00:11:17.085090+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=63694.1
- Funnel: target 782 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +83.36% | $126,898,400.65 |
| ESPORTS/USDT:USDT | +73.75% | $24,407,076.80 |
| STG/USDT:USDT | +20.87% | $14,810,591.31 |
| UB/USDT:USDT | +19.76% | $1,825,447.33 |
| XPL/USDT:USDT | +18.24% | $2,491,480.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SIREN/USDT:USDT | below_1h_threshold | +3.67% | +3.51% |
| BILL/USDT:USDT | below_1h_threshold | +2.18% | +2.02% |
| UB/USDT:USDT | below_1h_threshold | +2.05% | +1.89% |
| VELVET/USDT:USDT | below_1h_threshold | +2.03% | +1.87% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.77% | +1.61% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
