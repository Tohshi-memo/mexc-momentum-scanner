# Decision Report

- generated_at: 2026-06-10T21:49:55.386396+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6268**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6268, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.41% | **-0.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +1.87% | **+0.93%** |
| ASK | 20/20 | 100.0% | +0.50% | **+0.50%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.57% | **+0.40%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.47% | **+0.81%** |
| ASK_LONG | 20/20 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.00% | **+0.50%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.81% | **+0.41%** |
| MARKET_LONG | 20/20 | 100.0% | +0.41% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$150.46** / 初期 $100.00 (+50.46%)
- 確定: 1254件 (Win 314 / Loss 391 / Flat 549) / skip 1575件
- 成長率目線: 平均log +0.000326 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $150.46

## 4. Latest Market Context

- 更新: 2026-06-10T21:49:48.681843+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.34% price=61560.4
- Funnel: target 785 → liquid 154 → pre 50 → checked 50 → surge 5 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.5 >= 65=1, 4h RSI 70.9 >= 65=1, 4h RSI 88.4 >= 65=1, 4h RSI 70.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +50.57% | $32,023,381.42 |
| BEAT/USDT:USDT | +36.27% | $159,697,736.18 |
| STRAX/USDT:USDT | +13.02% | $1,240,212.08 |
| FOLKS/USDT:USDT | +8.02% | $11,884,759.33 |
| SKYAI/USDT:USDT | +6.48% | $5,948,339.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SIREN/USDT:USDT | below_1h_threshold | +3.82% | +4.17% |
| MYX/USDT:USDT | below_1h_threshold | +3.20% | +3.54% |
| LAB/USDT:USDT | below_1h_threshold | +2.71% | +3.05% |
| XMR/USDT:USDT | below_1h_threshold | +0.82% | +1.17% |
| SNT/USDT:USDT | below_1h_threshold | +0.82% | +1.16% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
