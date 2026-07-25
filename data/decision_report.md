# Decision Report

- generated_at: 2026-07-25T16:31:23.469789+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9531**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9531, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.69% | **-1.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_BB3S | 4/17 | 23.5% | +1.30% | **+0.31%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | -0.19% | **-0.03%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.51% | **+2.64%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.83% | **+2.41%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.88% | **+2.13%** |
| MARKET_LONG | 20/20 | 100.0% | +1.27% | **+1.27%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +2.33% | **+0.82%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$447.98** / 初期 $100.00 (+347.98%)
- 確定: 3359件 (Win 1064 / Loss 1088 / Flat 1207) / skip 2733件
- 成長率目線: 平均log +0.000446 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $447.98

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.02** / 初期 $100.00 (+36.02%)
- 確定: 1184件 (Win 324 / Loss 258 / Flat 602) / skip 1758件
- 成長率目線: 平均log +0.000260 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1670 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $136.02

## 5. Causal Adaptive DryRun ($100)

- 残高: **$107.77** / 初期 $100.00 (+7.77%)
- 確定: 577件 (Win 195 / Loss 221 / Flat 161) / pending 6件 / skip 422件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000538 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $107.77

## 6. Latest Market Context

- 更新: 2026-07-25T16:31:15.348103+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=64118.6
- Funnel: target 898 → liquid 138 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.0 >= 65=1, 4h RSI 73.4 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +13.96% | $88,381,946.39 |
| DEXE/USDT:USDT | +13.74% | $134,426,425.11 |
| ESPORTS/USDT:USDT | +6.75% | $22,173,021.90 |
| EUL/USDT:USDT | +5.02% | $13,769,883.03 |
| ZAMA/USDT:USDT | +3.03% | $6,520,579.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EUL/USDT:USDT | below_1h_threshold | +4.75% | +4.80% |
| ZAMA/USDT:USDT | below_1h_threshold | +3.03% | +3.08% |
| FLOKI/USDT:USDT | below_1h_threshold | +2.86% | +2.91% |
| RIF/USDT:USDT | below_1h_threshold | +2.22% | +2.27% |
| SHIB/USDT:USDT | below_1h_threshold | +2.06% | +2.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
