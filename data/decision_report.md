# Decision Report

- generated_at: 2026-11-13T09:36:41.488857+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18807**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18807, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.18% | **+0.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.34% | **+0.31%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| MARKET | 20/20 | 100.0% | +0.18% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +3.38% | **+1.18%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.64% | **+1.07%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.03% | **+0.92%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.77% | **+0.69%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.64% | **+0.66%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 273件 (TP 99 / SL 166 / EXP 8)
- 最新: IDOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,769.96** / 初期 $100.00 (+1669.96%)
- 確定: 7277件 (Win 2097 / Loss 2331 / Flat 2849) / skip 8091件
- 成長率目線: 平均log +0.000395 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $1,769.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$400.24** / 初期 $100.00 (+300.24%)
- 確定: 4822件 (Win 1300 / Loss 1074 / Flat 2448) / skip 7396件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0577 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.35% 残高後 $400.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6969件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000189 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-13T09:36:26.028642+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.56% price=69063.7
- Funnel: target 1086 → liquid 153 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +101.82% | $16,253,369.77 |
| BARD/USDT:USDT | +58.20% | $13,998,643.39 |
| ARIA/USDT:USDT | +41.09% | $9,886,706.64 |
| KOR/USDT:USDT | +32.12% | $1,818,124.41 |
| GANG/USDT:USDT | +16.54% | $1,237,888.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GANG/USDT:USDT | below_1h_threshold | +4.38% | +3.82% |
| H/USDT:USDT | below_1h_threshold | +2.92% | +2.36% |
| UAI/USDT:USDT | below_1h_threshold | +1.96% | +1.40% |
| SOXS/USDT:USDT | below_1h_threshold | +1.91% | +1.35% |
| BEAT/USDT:USDT | below_1h_threshold | +1.77% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
