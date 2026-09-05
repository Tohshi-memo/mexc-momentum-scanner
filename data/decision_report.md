# Decision Report

- generated_at: 2026-09-05T04:16:09.374689+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13697**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13697, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-3.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -3.02% | **-3.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 9/20 | 45.0% | +4.18% | **+1.88%** |
| LIMIT_9PCT | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_8PCT | 6/20 | 30.0% | +3.28% | **+0.99%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.96% | **+0.88%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.85% | **+1.85%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.02% | **+1.81%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.89% | **+1.60%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.68% | **+1.26%** |
| MARKET_LONG | 20/20 | 100.0% | +1.23% | **+1.23%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 202件 (TP 75 / SL 122 / EXP 5)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$855.36** / 初期 $100.00 (+755.36%)
- 確定: 5012件 (Win 1516 / Loss 1645 / Flat 1851) / skip 5246件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 4/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $855.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.15** / 初期 $100.00 (+88.15%)
- 確定: 2444件 (Win 690 / Loss 584 / Flat 1170) / skip 4664件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0838 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $188.15

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.31** / 初期 $100.00 (+18.31%)
- 確定: 2330件 (Win 695 / Loss 894 / Flat 741) / pending 5件 / skip 2834件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000340 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.31

## 6. Latest Market Context

- 更新: 2026-09-05T04:16:01.405402+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=79498.5
- Funnel: target 1050 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +86.49% | $5,638,530.59 |
| 4/USDT:USDT | +65.31% | $14,623,473.28 |
| AKE/USDT:USDT | +55.85% | $10,448,171.94 |
| DASH/USDT:USDT | +28.08% | $35,828,409.62 |
| ZEN/USDT:USDT | +19.94% | $8,447,247.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BULLA/USDT:USDT | below_1h_threshold | +3.30% | +3.36% |
| UP/USDT:USDT | below_1h_threshold | +2.95% | +3.01% |
| TUT/USDT:USDT | below_1h_threshold | +1.72% | +1.78% |
| DASH/USDT:USDT | below_1h_threshold | +1.54% | +1.59% |
| ZEN/USDT:USDT | below_1h_threshold | +1.40% | +1.46% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
