# Decision Report

- generated_at: 2026-09-05T03:06:13.699725+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13689**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13689, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.39% | **-0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.33% | **-0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/8 | 50.0% | +3.75% | **+1.88%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.68% | **+1.51%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.67% | **+1.33%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.38% | **+1.18%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +4.53% | **+1.13%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 202件 (TP 75 / SL 122 / EXP 5)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$855.36** / 初期 $100.00 (+755.36%)
- 確定: 5012件 (Win 1516 / Loss 1645 / Flat 1851) / skip 5238件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 4/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $855.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$189.99** / 初期 $100.00 (+89.99%)
- 確定: 2437件 (Win 689 / Loss 580 / Flat 1168) / skip 4663件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0957 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $189.99

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.83** / 初期 $100.00 (+18.83%)
- 確定: 2323件 (Win 694 / Loss 890 / Flat 739) / pending 4件 / skip 2834件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000429 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.83

## 6. Latest Market Context

- 更新: 2026-09-05T03:06:04.209889+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=79518.3
- Funnel: target 1050 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +63.44% | $13,783,684.94 |
| BULLA/USDT:USDT | +44.06% | $4,061,976.71 |
| AKE/USDT:USDT | +43.89% | $8,763,746.51 |
| DASH/USDT:USDT | +26.25% | $33,953,780.04 |
| ZEN/USDT:USDT | +20.35% | $7,825,840.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +2.09% | +2.10% |
| NIULAI/USDT:USDT | below_1h_threshold | +1.71% | +1.73% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.18% | +1.19% |
| NEAR/USDT:USDT | below_1h_threshold | +0.86% | +0.87% |
| FILECOIN/USDT:USDT | below_1h_threshold | +0.52% | +0.54% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
