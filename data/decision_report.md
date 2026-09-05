# Decision Report

- generated_at: 2026-09-05T03:16:25.205360+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13690**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13690, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.74% | **-0.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.33% | **-0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.23% | **+2.01%** |
| LIMIT_BB3S_LONG | 4/8 | 50.0% | +3.75% | **+1.88%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.84% | **+1.38%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +4.18% | **+1.25%** |
| MARKET_LONG | 20/20 | 100.0% | +1.14% | **+1.14%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 202件 (TP 75 / SL 122 / EXP 5)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$855.36** / 初期 $100.00 (+755.36%)
- 確定: 5012件 (Win 1516 / Loss 1645 / Flat 1851) / skip 5239件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 4/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $855.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$189.99** / 初期 $100.00 (+89.99%)
- 確定: 2438件 (Win 689 / Loss 580 / Flat 1169) / skip 4663件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1029 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $189.99

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.83** / 初期 $100.00 (+18.83%)
- 確定: 2324件 (Win 694 / Loss 890 / Flat 740) / pending 5件 / skip 2834件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000431 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $118.83

## 6. Latest Market Context

- 更新: 2026-09-05T03:16:12.651576+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=79555.0
- Funnel: target 1050 → liquid 160 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +74.48% | $13,954,750.44 |
| BULLA/USDT:USDT | +48.64% | $4,280,545.16 |
| AKE/USDT:USDT | +42.53% | $8,930,267.28 |
| DASH/USDT:USDT | +24.77% | $34,668,511.26 |
| ZEN/USDT:USDT | +17.90% | $7,997,023.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4/USDT:USDT | below_1h_threshold | +3.48% | +3.45% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +2.38% | +2.34% |
| SNXX/USDT:USDT | below_1h_threshold | +2.09% | +2.06% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.18% | +1.15% |
| ENJ/USDT:USDT | below_1h_threshold | +1.08% | +1.05% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
