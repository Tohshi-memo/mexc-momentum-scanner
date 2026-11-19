# Decision Report

- generated_at: 2026-11-19T05:16:11.185441+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19179**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.69% / filled 20/20。**
- 全期間 MARKET基準: n=19179, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.69% | **+1.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +2.17% | **+2.17%** |
| MARKET | 20/20 | 100.0% | +1.69% | **+1.69%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.73% | **+1.47%** |
| LIMIT_ATR | 15/20 | 75.0% | +1.61% | **+1.21%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.41% | **+0.98%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.43% | **+0.49%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +0.51% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 282件 (TP 102 / SL 172 / EXP 8)
- 最新: KORU/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,727.67** / 初期 $100.00 (+1627.67%)
- 確定: 7368件 (Win 2116 / Loss 2366 / Flat 2886) / skip 8372件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET` TP_HIT account +1.00% 残高後 $1,727.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$430.70** / 初期 $100.00 (+330.70%)
- 確定: 5022件 (Win 1335 / Loss 1087 / Flat 2600) / skip 7568件
- 成長率目線: 平均log +0.000291 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $430.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7338件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000237 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-19T05:16:02.050023+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=63412.2
- Funnel: target 1080 → liquid 142 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +30.55% | $9,406,460.91 |
| LUNC/USDT:USDT | +21.06% | $2,337,419.32 |
| VELVET/USDT:USDT | +19.75% | $4,671,168.03 |
| HUMA/USDT:USDT | +13.05% | $2,620,745.63 |
| BLESS/USDT:USDT | +10.91% | $21,575,776.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BULLA/USDT:USDT | below_1h_threshold | +3.11% | +3.34% |
| IRYS/USDT:USDT | below_1h_threshold | +1.22% | +1.44% |
| ARIA/USDT:USDT | below_1h_threshold | +1.01% | +1.23% |
| CSOPSKHYNIX2L/USDT:USDT | below_1h_threshold | +0.73% | +0.95% |
| LUNC/USDT:USDT | below_1h_threshold | +0.67% | +0.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
