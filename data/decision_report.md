# Decision Report

- generated_at: 2026-06-17T21:25:08.320687+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6968**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6968, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.26% | **-0.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.58% | **+0.17%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.00% | **-0.00%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +4.81% | **+2.89%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.96% | **+1.57%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.14% | **+1.39%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.69% | **+1.27%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.95% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$198.71** / 初期 $100.00 (+98.71%)
- 確定: 1818件 (Win 496 / Loss 573 / Flat 749) / skip 1711件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $198.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$103.62** / 初期 $100.00 (+3.62%)
- 確定: 241件 (Win 64 / Loss 59 / Flat 118) / skip 138件
- 成長率目線: 平均log +0.000148 / 幾何平均 +0.015% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0786 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAC/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $103.62

## 5. Latest Market Context

- 更新: 2026-06-17T21:25:04.120510+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=64332.2
- Funnel: target 790 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| O/USDT:USDT | +75.41% | $1,154,775.43 |
| SYN/USDT:USDT | +57.15% | $3,001,131.38 |
| RE/USDT:USDT | +13.63% | $1,730,871.69 |
| TAC/USDT:USDT | +11.46% | $2,511,306.97 |
| MITO/USDT:USDT | +9.00% | $1,527,698.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_1h_threshold | +3.78% | +3.90% |
| FOLKS/USDT:USDT | below_1h_threshold | +2.86% | +2.97% |
| ALLO/USDT:USDT | below_1h_threshold | +2.60% | +2.71% |
| UP/USDT:USDT | below_1h_threshold | +1.57% | +1.68% |
| ETHFI/USDT:USDT | below_1h_threshold | +1.18% | +1.29% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
