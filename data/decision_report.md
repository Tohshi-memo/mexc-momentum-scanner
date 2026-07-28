# Decision Report

- generated_at: 2026-07-28T07:46:35.604101+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9681**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9681, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.76% | **+0.97%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.19% | **+0.53%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.56% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.87% | **+1.87%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.95% | **+0.98%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +3.03% | **+0.91%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.31% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$106.92** / 初期 $100.00 (+6.92%)
- 確定トレード: 148件 (TP 51 / SL 92 / EXP 5)
- 最新: BANK/USDT:USDT TP_HIT PnL +8.00% 残高後 $106.92
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$469.75** / 初期 $100.00 (+369.75%)
- 確定: 3451件 (Win 1091 / Loss 1119 / Flat 1241) / skip 2791件
- 成長率目線: 平均log +0.000448 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $469.75

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1225件 (Win 338 / Loss 275 / Flat 612) / skip 1867件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0413 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 701件 (Win 226 / Loss 269 / Flat 206) / pending 4件 / skip 447件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000115 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $107.73

## 6. Latest Market Context

- 更新: 2026-07-28T07:46:25.305550+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=63456.3
- Funnel: target 898 → liquid 175 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COTI/USDT:USDT | +50.14% | $14,957,873.33 |
| DEXE/USDT:USDT | +26.99% | $14,813,686.85 |
| RIF/USDT:USDT | +14.45% | $7,555,599.38 |
| BULLA/USDT:USDT | +12.92% | $1,403,815.42 |
| SOONNETWORK/USDT:USDT | +12.48% | $1,724,668.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOONNETWORK/USDT:USDT | below_1h_threshold | +2.10% | +2.34% |
| PIPPIN/USDT:USDT | below_1h_threshold | +1.52% | +1.76% |
| AKE/USDT:USDT | below_1h_threshold | +1.35% | +1.59% |
| CAP/USDT:USDT | below_1h_threshold | +0.90% | +1.14% |
| ESPORTS/USDT:USDT | below_1h_threshold | +0.46% | +0.70% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
