# Decision Report

- generated_at: 2026-07-02T20:00:46.258977+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8101**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8101, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.14% | **-1.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +3.73% | **+0.75%** |
| LIMIT_9PCT | 4/20 | 20.0% | +3.29% | **+0.66%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | +2.22% | **+0.44%** |
| LIMIT_BB3S | 4/16 | 25.0% | +0.05% | **+0.01%** |
| LIMIT_7PCT | 6/20 | 30.0% | -0.60% | **-0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.96% | **+2.07%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.69% | **+1.88%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.70% | **+1.80%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.92% | **+1.53%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.40% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$103.14** / 初期 $100.00 (+3.14%)
- 確定トレード: 52件 (TP 19 / SL 32 / EXP 1)
- 最新: TAIKO/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.14
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.67** / 初期 $100.00 (+184.67%)
- 確定: 2444件 (Win 754 / Loss 816 / Flat 874) / skip 2218件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $284.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.14** / 初期 $100.00 (+5.14%)
- 確定: 561件 (Win 136 / Loss 131 / Flat 294) / skip 951件
- 成長率目線: 平均log +0.000089 / 幾何平均 +0.009% per trade / maxDD +3.53%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0354 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAIKO/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $105.14

## 5. Latest Market Context

- 更新: 2026-07-02T20:00:40.394978+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=61439.0
- Funnel: target 834 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +21.13% | $4,158,486.44 |
| TAIKO/USDT:USDT | +18.21% | $101,082,749.96 |
| BASED/USDT:USDT | +17.37% | $13,994,563.96 |
| ALLO/USDT:USDT | +11.89% | $20,373,131.65 |
| RIF/USDT:USDT | +8.26% | $5,921,211.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +0.82% | +0.84% |
| AAVE/USDT:USDT | below_1h_threshold | +0.28% | +0.30% |
| PIPPIN/USDT:USDT | below_1h_threshold | +0.26% | +0.28% |
| VELVET/USDT:USDT | below_1h_threshold | +0.21% | +0.23% |
| US/USDT:USDT | below_1h_threshold | +0.19% | +0.22% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
