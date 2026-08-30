# Decision Report

- generated_at: 2026-08-30T06:26:14.998799+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13027**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13027, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 14/17 | 82.4% | +1.87% | **+1.54%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.26% | **+0.57%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.06% | **+0.42%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.17% | **+0.09%** |
| LIMIT_7PCT | 4/20 | 20.0% | -0.60% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.58% | **+1.16%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_FIB1272_LONG | 2/20 | 10.0% | +7.32% | **+0.73%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$785.19** / 初期 $100.00 (+685.19%)
- 確定: 4797件 (Win 1461 / Loss 1578 / Flat 1758) / skip 4791件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HNT/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $785.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$174.30** / 初期 $100.00 (+74.30%)
- 確定: 2111件 (Win 591 / Loss 514 / Flat 1006) / skip 4327件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0564 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HNT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $174.30

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.02** / 初期 $100.00 (+17.02%)
- 確定: 2070件 (Win 608 / Loss 803 / Flat 659) / pending 5件 / skip 2425件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000265 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HNT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.02

## 6. Latest Market Context

- 更新: 2026-08-30T06:26:06.232278+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=78155.7
- Funnel: target 1023 → liquid 116 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HNT/USDT:USDT | +81.31% | $35,019,268.37 |
| NIULAI/USDT:USDT | +69.54% | $2,775,484.06 |
| FONE/USDT:USDT | +53.25% | $1,441,024.51 |
| PONS/USDT:USDT | +49.12% | $1,568,581.64 |
| SKR/USDT:USDT | +30.63% | $1,904,838.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIULAI/USDT:USDT | below_1h_threshold | +4.99% | +4.93% |
| MOVR/USDT:USDT | below_1h_threshold | +4.11% | +4.05% |
| PONS/USDT:USDT | below_1h_threshold | +2.88% | +2.82% |
| HEMI/USDT:USDT | below_1h_threshold | +2.84% | +2.78% |
| UAI/USDT:USDT | below_1h_threshold | +2.36% | +2.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
