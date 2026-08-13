# Decision Report

- generated_at: 2026-08-13T15:56:31.395466+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11456**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11456, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.94% | **-1.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 18/20 | 90.0% | +0.36% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.08% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +5.00% | **+2.00%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +4.57% | **+1.60%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.43% | **+1.58%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +1.46% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.88** / 初期 $100.00 (+516.88%)
- 確定: 3974件 (Win 1240 / Loss 1299 / Flat 1435) / skip 4043件
- 成長率目線: 平均log +0.000458 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COTI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $616.88

## 4. Robust Adaptive DryRun ($100)

- 残高: **$152.59** / 初期 $100.00 (+52.59%)
- 確定: 1644件 (Win 471 / Loss 392 / Flat 781) / skip 3223件
- 成長率目線: 平均log +0.000257 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0886 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $152.59

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.30** / 初期 $100.00 (+17.30%)
- 確定: 1459件 (Win 431 / Loss 548 / Flat 480) / pending 6件 / skip 1467件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000292 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $117.30

## 6. Latest Market Context

- 更新: 2026-08-13T15:56:22.036782+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.39% price=63587.5
- Funnel: target 978 → liquid 176 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.1 >= 65=1, 4h RSI 81.9 >= 65=1, 4h RSI 85.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +60.80% | $27,563,819.39 |
| COTI/USDT:USDT | +31.72% | $12,147,304.06 |
| AVAAI/USDT:USDT | +30.30% | $1,970,874.65 |
| ACU/USDT:USDT | +28.78% | $8,196,782.23 |
| SNXX/USDT:USDT | +22.73% | $9,962,357.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SMCISTOCK/USDT:USDT | below_1h_threshold | +4.78% | +5.17% |
| COTI/USDT:USDT | below_1h_threshold | +4.59% | +4.98% |
| APR/USDT:USDT | below_1h_threshold | +4.02% | +4.40% |
| MYX/USDT:USDT | below_1h_threshold | +3.30% | +3.69% |
| MUU/USDT:USDT | below_1h_threshold | +3.30% | +3.69% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
