# Decision Report

- generated_at: 2026-10-01T11:12:03.276110+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15898**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15898, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.61% | **-1.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +0.95% | **+0.48%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +0.59% | **+0.09%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.05% | **+0.04%** |
| LIMIT_ATR | 17/20 | 85.0% | -0.06% | **-0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 9/11 | 81.8% | +2.63% | **+2.15%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.14% | **+1.92%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.32% | **+1.51%** |
| MARKET_LONG | 20/20 | 100.0% | +1.29% | **+1.29%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.73% | **+0.95%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,296.94** / 初期 $100.00 (+1196.94%)
- 確定: 6016件 (Win 1782 / Loss 1935 / Flat 2299) / skip 6443件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACNSTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.70% 残高後 $1,296.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$270.41** / 初期 $100.00 (+170.41%)
- 確定: 3551件 (Win 983 / Loss 816 / Flat 1752) / skip 5758件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1262 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACNSTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.47% 残高後 $270.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4058件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000288 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T11:11:49.302769+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=83872.9
- Funnel: target 1097 → liquid 173 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MOVR/USDT:USDT | +71.37% | $17,203,225.22 |
| LONGXIA/USDT:USDT | +49.82% | $3,316,768.86 |
| NOM/USDT:USDT | +28.01% | $2,565,147.85 |
| CT/USDT:USDT | +26.14% | $6,387,825.72 |
| NIGHT/USDT:USDT | +20.43% | $8,544,829.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LONGXIA/USDT:USDT | below_1h_threshold | +3.40% | +3.47% |
| CT/USDT:USDT | below_1h_threshold | +2.46% | +2.53% |
| MOVR/USDT:USDT | below_1h_threshold | +1.93% | +2.00% |
| KORU/USDT:USDT | below_1h_threshold | +1.47% | +1.53% |
| SNXX/USDT:USDT | below_1h_threshold | +1.34% | +1.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
