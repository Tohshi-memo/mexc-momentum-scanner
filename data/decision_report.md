# Decision Report

- generated_at: 2026-11-13T07:46:32.229370+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18800**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18800, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.28% | **-0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.95% | **+0.90%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.86% | **+1.12%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.41% | **+0.97%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.47% | **+0.81%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.93% | **+0.79%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.87% | **+0.78%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 273件 (TP 99 / SL 166 / EXP 8)
- 最新: IDOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,758.99** / 初期 $100.00 (+1658.99%)
- 確定: 7270件 (Win 2095 / Loss 2329 / Flat 2846) / skip 8091件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KOR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,758.99

## 4. Robust Adaptive DryRun ($100)

- 残高: **$401.34** / 初期 $100.00 (+301.34%)
- 確定: 4819件 (Win 1299 / Loss 1072 / Flat 2448) / skip 7392件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0366 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $401.34

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6960件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000195 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-13T07:46:16.240890+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.38% price=68776.3
- Funnel: target 1086 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +53.18% | $12,412,566.86 |
| BARD/USDT:USDT | +48.56% | $11,508,599.97 |
| ARIA/USDT:USDT | +34.68% | $9,630,933.15 |
| KOR/USDT:USDT | +33.33% | $1,768,590.34 |
| KGEN/USDT:USDT | +15.67% | $2,690,258.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +3.90% | +4.29% |
| UAI/USDT:USDT | below_1h_threshold | +3.52% | +3.90% |
| PONS/USDT:USDT | below_1h_threshold | +3.11% | +3.49% |
| H/USDT:USDT | below_1h_threshold | +2.96% | +3.34% |
| Q/USDT:USDT | below_1h_threshold | +2.00% | +2.38% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
