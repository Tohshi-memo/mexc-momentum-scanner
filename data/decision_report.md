# Decision Report

- generated_at: 2026-08-30T10:26:17.397752+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13049**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.19% / filled 20/20。**
- 全期間 MARKET基準: n=13049, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.19% | **+1.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.15% | **+1.09%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.73% | **+0.35%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.10% | **+0.07%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.03% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +0.64% | **+0.64%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.01% | **+0.51%** |
| MARKET_LONG | 20/20 | 100.0% | +0.39% | **+0.39%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.06% | **+0.05%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$774.74** / 初期 $100.00 (+674.74%)
- 確定: 4807件 (Win 1463 / Loss 1584 / Flat 1760) / skip 4803件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $774.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$171.79** / 初期 $100.00 (+71.79%)
- 確定: 2133件 (Win 593 / Loss 519 / Flat 1021) / skip 4327件
- 成長率目線: 平均log +0.000254 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0267 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZKC/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $171.79

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.50** / 初期 $100.00 (+16.50%)
- 確定: 2080件 (Win 610 / Loss 809 / Flat 661) / pending 3件 / skip 2437件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000157 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.50

## 6. Latest Market Context

- 更新: 2026-08-30T10:26:08.617917+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=78032.8
- Funnel: target 1026 → liquid 121 → pre 50 → checked 49 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=1
- Strict後reject: 4h RSI 80.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +79.79% | $5,253,201.44 |
| HNT/USDT:USDT | +72.43% | $43,083,480.40 |
| SKR/USDT:USDT | +57.41% | $2,803,490.27 |
| ZKC/USDT:USDT | +54.61% | $2,182,290.04 |
| PONS/USDT:USDT | +52.15% | $1,802,727.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FONE/USDT:USDT | below_1h_threshold | +4.02% | +3.94% |
| DOS/USDT:USDT | below_1h_threshold | +3.50% | +3.42% |
| SKR/USDT:USDT | below_1h_threshold | +3.05% | +2.97% |
| BTR/USDT:USDT | below_1h_threshold | +2.78% | +2.70% |
| NIULAI/USDT:USDT | below_1h_threshold | +2.56% | +2.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
