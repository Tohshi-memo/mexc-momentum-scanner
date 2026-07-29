# Decision Report

- generated_at: 2026-07-29T04:36:13.906727+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9773**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9773, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.07% | **+0.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +1.58% | **+1.18%** |
| LIMIT_10PCT | 3/20 | 15.0% | +6.30% | **+0.95%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | +1.21% | **+0.73%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.94% | **+0.66%** |
| LIMIT_BB3S | 7/17 | 41.2% | +1.15% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +6.73% | **+1.35%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.81% | **+1.26%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.68% | **+0.94%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.03% | **+0.46%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.65% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$119.87** / 初期 $100.00 (+19.87%)
- 確定トレード: 161件 (TP 63 / SL 93 / EXP 5)
- 最新: MUSTOCK/USDT:USDT TP_HIT PnL +7.86% 残高後 $119.87
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3519件 (Win 1113 / Loss 1147 / Flat 1259) / skip 2815件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1227件 (Win 338 / Loss 275 / Flat 614) / skip 1957件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0226 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EUL/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.16** / 初期 $100.00 (+10.16%)
- 確定: 760件 (Win 246 / Loss 291 / Flat 223) / pending 0件 / skip 481件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000498 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $110.16

## 6. Latest Market Context

- 更新: 2026-07-29T04:36:06.993483+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=63809.5
- Funnel: target 904 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +55.90% | $1,519,614.59 |
| BTW/USDT:USDT | +31.85% | $7,203,674.68 |
| BEAT/USDT:USDT | +14.80% | $44,952,686.98 |
| EUL/USDT:USDT | +14.17% | $2,847,685.34 |
| SOXS/USDT:USDT | +13.13% | $8,995,771.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EUL/USDT:USDT | below_1h_threshold | +3.50% | +3.37% |
| ON/USDT:USDT | below_1h_threshold | +3.37% | +3.23% |
| SOXS/USDT:USDT | below_1h_threshold | +3.27% | +3.13% |
| RIF/USDT:USDT | below_1h_threshold | +2.51% | +2.38% |
| AGT/USDT:USDT | below_1h_threshold | +2.14% | +2.01% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
