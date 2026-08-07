# Decision Report

- generated_at: 2026-08-07T17:11:24.703038+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10736**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10736, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.01% | **+0.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +0.64% | **+0.45%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.27% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.80% | **+0.64%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.37% | **+0.24%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.38% | **+0.23%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.08% | **+0.03%** |
| MARKET_LONG | 20/20 | 100.0% | -0.06% | **-0.06%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3799件 (Win 1203 / Loss 1250 / Flat 1346) / skip 3498件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AXTISTOCK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.80** / 初期 $100.00 (+44.80%)
- 確定: 1461件 (Win 410 / Loss 342 / Flat 709) / skip 2686件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0147 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $144.80

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.24** / 初期 $100.00 (+18.24%)
- 確定: 1178件 (Win 380 / Loss 465 / Flat 333) / pending 4件 / skip 1033件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000157 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CYS/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.24

## 6. Latest Market Context

- 更新: 2026-08-07T17:11:15.948633+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=64727.4
- Funnel: target 961 → liquid 190 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EPIC/USDT:USDT | +13.19% | $1,746,164.62 |
| HEI/USDT:USDT | +9.54% | $24,462,387.15 |
| C98/USDT:USDT | +6.80% | $2,132,211.02 |
| ACE/USDT:USDT | +6.51% | $34,193,636.48 |
| BICO/USDT:USDT | +6.37% | $32,560,991.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZBT/USDT:USDT | below_1h_threshold | +2.12% | +2.20% |
| C98/USDT:USDT | below_1h_threshold | +2.00% | +2.08% |
| ALLO/USDT:USDT | below_1h_threshold | +1.75% | +1.84% |
| BEAT/USDT:USDT | below_1h_threshold | +1.39% | +1.47% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +1.26% | +1.34% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
