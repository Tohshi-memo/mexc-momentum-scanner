# Decision Report

- generated_at: 2026-08-08T03:26:22.797441+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10797**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.78% / filled 20/20。**
- 全期間 MARKET基準: n=10797, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_7PCT | 7/20 | 35.0% | +1.37% | **+0.48%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.11% | **+0.39%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.20% | **+0.18%** |
| LIMIT_8PCT | 6/20 | 30.0% | +0.57% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +4.64% | **+1.16%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +1.71% | **+0.94%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +2.25% | **+0.90%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +1.25% | **+0.62%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.90% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$601.56** / 初期 $100.00 (+501.56%)
- 確定: 3801件 (Win 1204 / Loss 1250 / Flat 1347) / skip 3557件
- 成長率目線: 平均log +0.000472 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_6PCT` TP_HIT account +1.00% 残高後 $601.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1510件 (Win 424 / Loss 360 / Flat 726) / skip 2698件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0463 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.02** / 初期 $100.00 (+18.02%)
- 確定: 1182件 (Win 381 / Loss 468 / Flat 333) / pending 0件 / skip 1086件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000121 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AXTISTOCK/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.02

## 6. Latest Market Context

- 更新: 2026-08-08T03:26:13.339593+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=64969.4
- Funnel: target 961 → liquid 180 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +154.56% | $4,860,064.97 |
| BLESS/USDT:USDT | +35.12% | $93,694,365.11 |
| MMT/USDT:USDT | +16.35% | $1,291,246.97 |
| BSB/USDT:USDT | +13.60% | $2,899,654.06 |
| CYS/USDT:USDT | +12.85% | $16,269,795.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RBRKSTOCK/USDT:USDT | below_1h_threshold | +4.20% | +4.08% |
| CYS/USDT:USDT | below_1h_threshold | +1.98% | +1.86% |
| TUT/USDT:USDT | below_1h_threshold | +1.82% | +1.70% |
| CAP/USDT:USDT | below_1h_threshold | +1.72% | +1.60% |
| AKE/USDT:USDT | below_1h_threshold | +1.61% | +1.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
