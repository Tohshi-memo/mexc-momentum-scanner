# Decision Report

- generated_at: 2026-10-23T15:26:35.464224+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17225**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17225, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.94% | **-1.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +1.18% | **+0.47%** |
| LIMIT_BB3S | 6/19 | 31.6% | +0.97% | **+0.31%** |
| LIMIT_7PCT | 4/20 | 20.0% | +0.70% | **+0.14%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.52% | **+0.13%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.17% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.82% | **+2.39%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +4.13% | **+2.27%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +3.91% | **+1.76%** |
| MARKET_LONG | 20/20 | 100.0% | +1.74% | **+1.74%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.95% | **+1.62%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,310.72** / 初期 $100.00 (+1210.72%)
- 確定: 6553件 (Win 1902 / Loss 2094 / Flat 2557) / skip 7233件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UNITREE/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,310.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.98** / 初期 $100.00 (+177.98%)
- 確定: 3889件 (Win 1061 / Loss 904 / Flat 1924) / skip 6747件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0582 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IRYS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $277.98

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5385件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000273 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-23T15:26:19.537198+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.23% price=81560.0
- Funnel: target 1088 → liquid 169 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.8 >= 65=1, 4h RSI 68.5 >= 65=1, 4h RSI 77.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +145.99% | $28,264,171.54 |
| BIRB/USDT:USDT | +40.42% | $2,054,145.68 |
| BTR/USDT:USDT | +39.49% | $15,706,715.14 |
| UNITREE/USDT:USDT | +22.03% | $6,113,232.55 |
| AKE/USDT:USDT | +13.93% | $16,126,957.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MVLL/USDT:USDT | below_1h_threshold | +2.41% | +2.64% |
| AKE/USDT:USDT | below_1h_threshold | +1.78% | +2.01% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +0.75% | +0.98% |
| ATH/USDT:USDT | below_1h_threshold | +0.59% | +0.82% |
| MUU/USDT:USDT | below_1h_threshold | +0.49% | +0.72% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
