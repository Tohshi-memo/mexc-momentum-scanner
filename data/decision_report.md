# Decision Report

- generated_at: 2026-06-16T12:04:13.921945+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6861**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6861, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.52% | **-0.16%** |
| LIMIT_3PCT | 16/20 | 80.0% | -1.16% | **-0.93%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +8.00% | **+5.33%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.22% | **+1.33%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.63% | **+1.22%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.49% | **+1.12%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.69% | **+0.93%** |

## 2. $100 Live Portfolio

- 残高: **$102.50** / 初期 $100.00 (+2.50%)
- 確定トレード: 10件 (TP 5 / SL 5 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.50
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$189.68** / 初期 $100.00 (+89.68%)
- 確定: 1734件 (Win 456 / Loss 539 / Flat 739) / skip 1688件
- 成長率目線: 平均log +0.000369 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $189.68

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 156件 (Win 28 / Loss 30 / Flat 98) / skip 116件
- 成長率目線: 平均log -0.000155 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0975 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-16T12:04:08.872317+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=66395.4
- Funnel: target 777 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +47.29% | $2,920,849.51 |
| PORTAL/USDT:USDT | +40.37% | $2,714,553.22 |
| BSB/USDT:USDT | +38.48% | $33,093,636.55 |
| SPACE/USDT:USDT | +27.32% | $4,398,488.38 |
| ROAM/USDT:USDT | +22.70% | $6,309,686.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +1.98% | +2.07% |
| ALLO/USDT:USDT | below_1h_threshold | +1.55% | +1.64% |
| PORTAL/USDT:USDT | below_1h_threshold | +1.36% | +1.45% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.91% | +1.00% |
| LAB/USDT:USDT | below_1h_threshold | +0.65% | +0.74% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
