# Decision Report

- generated_at: 2026-11-13T14:21:45.023113+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18824**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18824, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 6/20 | 30.0% | +6.86% | **+2.06%** |
| LIMIT_10PCT | 5/20 | 25.0% | +8.00% | **+2.00%** |
| LIMIT_8PCT | 8/20 | 40.0% | +4.35% | **+1.74%** |
| LIMIT_7PCT | 9/20 | 45.0% | +1.87% | **+0.84%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +1.53% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +4.19% | **+2.72%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.24% | **+1.78%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.20% | **+1.60%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.83% | **+1.56%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.50% | **+1.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 273件 (TP 99 / SL 166 / EXP 8)
- 最新: IDOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,763.10** / 初期 $100.00 (+1663.10%)
- 確定: 7289件 (Win 2100 / Loss 2337 / Flat 2852) / skip 8096件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BARD/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $1,763.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$396.05** / 初期 $100.00 (+296.05%)
- 確定: 4832件 (Win 1300 / Loss 1077 / Flat 2455) / skip 7403件
- 成長率目線: 平均log +0.000285 / 幾何平均 +0.028% per trade / maxDD +4.29%
- 次の候補: `LIMIT_8PCT` (selected_by_robust_growth_score) / robust_score +0.1331 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_8PCT` SL_HIT account -0.35% 残高後 $396.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6984件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000317 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-13T14:21:33.675459+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.47% price=69206.3
- Funnel: target 1083 → liquid 145 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.5 >= 65=1, 4h RSI 69.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +146.06% | $29,649,244.41 |
| BARD/USDT:USDT | +76.11% | $22,521,627.67 |
| KGEN/USDT:USDT | +27.04% | $1,033,341.67 |
| KOR/USDT:USDT | +24.54% | $1,909,520.68 |
| ARIA/USDT:USDT | +23.74% | $10,727,017.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| Q/USDT:USDT | below_1h_threshold | +2.06% | +2.53% |
| ORDI/USDT:USDT | below_1h_threshold | +0.78% | +1.25% |
| TESLA/USDT:USDT | below_1h_threshold | +0.61% | +1.08% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.60% | +1.07% |
| NVIDIA/USDT:USDT | below_1h_threshold | +0.59% | +1.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
