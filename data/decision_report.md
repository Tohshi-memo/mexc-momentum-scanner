# Decision Report

- generated_at: 2026-07-19T01:06:15.503884+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8989**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8989, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.95% | **-1.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | +2.35% | **+0.47%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_3PCT | 18/20 | 90.0% | +0.19% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.27% | **+1.82%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +3.99% | **+1.80%** |
| MARKET_LONG | 20/20 | 100.0% | +1.75% | **+1.75%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.79% | **+1.67%** |
| LIMIT_5PCT_LONG | 5/20 | 25.0% | +5.77% | **+1.44%** |

## 2. $100 Live Portfolio

- 残高: **$110.69** / 初期 $100.00 (+10.69%)
- 確定トレード: 116件 (TP 43 / SL 69 / EXP 4)
- 最新: B/USDT:USDT SL_HIT PnL -3.30% 残高後 $110.69
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$364.64** / 初期 $100.00 (+264.64%)
- 確定: 3052件 (Win 948 / Loss 973 / Flat 1131) / skip 2498件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $364.64

## 4. Robust Adaptive DryRun ($100)

- 残高: **$121.45** / 初期 $100.00 (+21.45%)
- 確定: 950件 (Win 238 / Loss 192 / Flat 520) / skip 1450件
- 成長率目線: 平均log +0.000205 / 幾何平均 +0.020% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1825 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $121.45

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.04** / 初期 $100.00 (-0.96%)
- 確定: 196件 (Win 62 / Loss 107 / Flat 27) / pending 0件 / skip 264件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000588 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RAVE/USDT:USDT `MARKET` EXPIRED account +0.16% 残高後 $99.04

## 6. Latest Market Context

- 更新: 2026-07-19T01:06:08.964266+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=64752.0
- Funnel: target 885 → liquid 122 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +83.80% | $29,501,116.27 |
| BANK/USDT:USDT | +42.30% | $18,532,468.94 |
| TLM/USDT:USDT | +25.75% | $2,821,067.55 |
| B/USDT:USDT | +18.72% | $32,505,042.56 |
| AKE/USDT:USDT | +17.82% | $82,840,834.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +3.54% | +3.54% |
| BANK/USDT:USDT | below_1h_threshold | +1.50% | +1.51% |
| BILL/USDT:USDT | below_1h_threshold | +1.47% | +1.48% |
| KAITO/USDT:USDT | below_1h_threshold | +0.87% | +0.88% |
| MYX/USDT:USDT | below_1h_threshold | +0.52% | +0.53% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
