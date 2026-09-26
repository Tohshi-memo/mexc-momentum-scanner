# Decision Report

- generated_at: 2026-09-26T14:11:14.769809+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15602**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15602, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.08% | **-0.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +0.63% | **+0.48%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.67% | **+0.40%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.00% | **+0.35%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.44% | **+0.35%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +3.42% | **+1.71%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +3.37% | **+1.52%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.10% | **+1.47%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.02% | **+1.11%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.42% | **+0.85%** |

## 2. $100 Live Portfolio

- 残高: **$120.87** / 初期 $100.00 (+20.87%)
- 確定トレード: 224件 (TP 82 / SL 135 / EXP 7)
- 最新: UNI/USDT:USDT EXPIRED PnL +1.69% 残高後 $120.87
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,256.31** / 初期 $100.00 (+1156.31%)
- 確定: 5963件 (Win 1762 / Loss 1915 / Flat 2286) / skip 6200件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MUBARAK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,256.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$264.01** / 初期 $100.00 (+164.01%)
- 確定: 3532件 (Win 974 / Loss 811 / Flat 1747) / skip 5481件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0907 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MUBARAK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $264.01

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.20** / 初期 $100.00 (+19.20%)
- 確定: 3187件 (Win 937 / Loss 1263 / Flat 987) / pending 1件 / skip 3882件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000315 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MUBARAK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $119.20

## 6. Latest Market Context

- 更新: 2026-09-26T14:11:05.734770+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=83898.0
- Funnel: target 1070 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PAID/USDT:USDT | +328.21% | $2,826,105.39 |
| RARE/USDT:USDT | +49.69% | $7,234,800.99 |
| BR/USDT:USDT | +31.24% | $10,692,312.75 |
| 2Z/USDT:USDT | +27.81% | $3,600,652.12 |
| BATON/USDT:USDT | +26.17% | $1,161,780.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PAID/USDT:USDT | below_1h_threshold | +3.89% | +3.90% |
| RARE/USDT:USDT | below_1h_threshold | +2.84% | +2.86% |
| BEAT/USDT:USDT | below_1h_threshold | +1.70% | +1.71% |
| BATON/USDT:USDT | below_1h_threshold | +0.85% | +0.86% |
| PYTH/USDT:USDT | below_1h_threshold | +0.70% | +0.72% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
