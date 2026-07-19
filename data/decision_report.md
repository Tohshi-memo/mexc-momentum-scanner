# Decision Report

- generated_at: 2026-07-19T05:11:06.163905+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9001**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9001, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.59% | **-0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.54% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.49% | **+2.24%** |
| MARKET_LONG | 20/20 | 100.0% | +1.77% | **+1.77%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.21% | **+1.44%** |
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +0.30% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$373.96** / 初期 $100.00 (+273.96%)
- 確定: 3063件 (Win 954 / Loss 977 / Flat 1132) / skip 2499件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAG/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.65% 残高後 $373.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$122.50** / 初期 $100.00 (+22.50%)
- 確定: 962件 (Win 242 / Loss 197 / Flat 523) / skip 1450件
- 成長率目線: 平均log +0.000211 / 幾何平均 +0.021% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2050 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAG/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $122.50

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.55** / 初期 $100.00 (-0.45%)
- 確定: 204件 (Win 65 / Loss 109 / Flat 30) / pending 3件 / skip 264件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000630 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TAG/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $99.55

## 6. Latest Market Context

- 更新: 2026-07-19T05:11:00.334716+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=64725.5
- Funnel: target 885 → liquid 122 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +131.24% | $38,119,601.98 |
| BANK/USDT:USDT | +43.21% | $17,820,333.91 |
| B/USDT:USDT | +26.85% | $36,205,794.51 |
| TAG/USDT:USDT | +18.18% | $1,179,640.49 |
| TLM/USDT:USDT | +15.40% | $3,176,734.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +2.97% | +2.91% |
| TAG/USDT:USDT | below_1h_threshold | +2.91% | +2.85% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.31% | +2.26% |
| HOME/USDT:USDT | below_1h_threshold | +1.75% | +1.70% |
| GALA/USDT:USDT | below_1h_threshold | +1.12% | +1.07% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
