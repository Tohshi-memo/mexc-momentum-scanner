# Decision Report

- generated_at: 2026-09-08T07:36:10.917434+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13968**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13968, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.36% | **-0.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.76% | **+0.97%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.20% | **+0.06%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.31% | **-0.20%** |
| MARKET | 20/20 | 100.0% | -0.36% | **-0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.03% | **+1.32%** |
| MARKET_LONG | 20/20 | 100.0% | +0.96% | **+0.96%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.16% | **+0.87%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +1.04% | **+0.83%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.02% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,020.05** / 初期 $100.00 (+920.05%)
- 確定: 5241件 (Win 1581 / Loss 1702 / Flat 1958) / skip 5288件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FORM/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $1,020.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$189.48** / 初期 $100.00 (+89.48%)
- 確定: 2573件 (Win 718 / Loss 618 / Flat 1237) / skip 4806件
- 成長率目線: 平均log +0.000248 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1226 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FORM/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $189.48

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.75** / 初期 $100.00 (+22.75%)
- 確定: 2557件 (Win 753 / Loss 959 / Flat 845) / pending 3件 / skip 2878件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000329 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FORM/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $122.75

## 6. Latest Market Context

- 更新: 2026-09-08T07:36:01.254714+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=78469.1
- Funnel: target 1065 → liquid 152 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOPH/USDT:USDT | +111.75% | $9,853,921.55 |
| FORM/USDT:USDT | +49.50% | $1,420,276.08 |
| MEMEROBINHOOD/USDT:USDT | +17.00% | $7,401,254.49 |
| AKE/USDT:USDT | +13.92% | $12,728,351.90 |
| AERO/USDT:USDT | +13.59% | $5,633,046.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COTI/USDT:USDT | below_1h_threshold | +3.02% | +2.79% |
| CAKE/USDT:USDT | below_1h_threshold | +2.90% | +2.67% |
| HAJIMI/USDT:USDT | below_1h_threshold | +2.72% | +2.50% |
| WLD/USDT:USDT | below_1h_threshold | +2.46% | +2.23% |
| XPL/USDT:USDT | below_1h_threshold | +2.06% | +1.83% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
