# Decision Report

- generated_at: 2026-09-04T10:11:31.916336+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13600**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13600, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.08% | **+0.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 19/20 | 95.0% | +0.94% | **+0.89%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.69% | **+0.69%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.25% | **+0.18%** |
| LIMIT_5PCT | 2/20 | 10.0% | +0.95% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.51% | **+1.28%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.48% | **+1.11%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.83% | **+0.83%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.70% | **+0.67%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.52% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5010件 (Win 1516 / Loss 1644 / Flat 1850) / skip 5151件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEST/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.90** / 初期 $100.00 (+85.90%)
- 確定: 2415件 (Win 681 / Loss 576 / Flat 1158) / skip 4596件
- 成長率目線: 平均log +0.000257 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0395 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKR/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $185.90

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.02** / 初期 $100.00 (+16.02%)
- 確定: 2253件 (Win 667 / Loss 878 / Flat 708) / pending 6件 / skip 2815件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000061 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SKR/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $116.02

## 6. Latest Market Context

- 更新: 2026-09-04T10:11:19.796930+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=80893.7
- Funnel: target 1052 → liquid 162 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| USELESS/USDT:USDT | +47.10% | $36,575,085.16 |
| TRIA/USDT:USDT | +45.78% | $7,050,149.75 |
| HNT/USDT:USDT | +24.09% | $13,450,139.24 |
| SKR/USDT:USDT | +23.75% | $5,088,589.38 |
| PONS/USDT:USDT | +14.89% | $10,274,693.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRIA/USDT:USDT | below_1h_threshold | +2.16% | +2.32% |
| HNT/USDT:USDT | below_1h_threshold | +1.76% | +1.91% |
| SKR/USDT:USDT | below_1h_threshold | +0.69% | +0.85% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +0.37% | +0.53% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +0.37% | +0.52% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
