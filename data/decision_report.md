# Decision Report

- generated_at: 2026-07-02T00:29:58.951303+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8038**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8038, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_10PCT | 7/20 | 35.0% | +0.42% | **+0.15%** |
| LIMIT_9PCT | 7/20 | 35.0% | +0.17% | **+0.06%** |
| LIMIT_6PCT | 10/20 | 50.0% | -1.01% | **-0.51%** |
| LIMIT_8PCT | 8/20 | 40.0% | -1.54% | **-0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.60% | **+2.60%** |
| ASK_LONG | 20/20 | 100.0% | +2.23% | **+2.23%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +2.48% | **+1.61%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.53% | **+1.52%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.84% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$291.91** / 初期 $100.00 (+191.91%)
- 確定: 2435件 (Win 752 / Loss 809 / Flat 874) / skip 2164件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SLX/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $291.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.51** / 初期 $100.00 (+5.51%)
- 確定: 544件 (Win 136 / Loss 130 / Flat 278) / skip 905件
- 成長率目線: 平均log +0.000099 / 幾何平均 +0.010% per trade / maxDD +3.19%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAIKO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $105.51

## 5. Latest Market Context

- 更新: 2026-07-02T00:29:51.877299+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.41% price=59754.7
- Funnel: target 825 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAIKO/USDT:USDT | +212.46% | $62,395,946.11 |
| TLM/USDT:USDT | +48.83% | $6,825,885.95 |
| SLX/USDT:USDT | +26.97% | $7,341,033.12 |
| RIF/USDT:USDT | +16.07% | $2,993,281.17 |
| BASED/USDT:USDT | +15.86% | $19,592,778.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +4.57% | +4.98% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +3.27% | +3.68% |
| BASED/USDT:USDT | below_1h_threshold | +2.90% | +3.31% |
| B/USDT:USDT | below_1h_threshold | +2.41% | +2.82% |
| ZBT/USDT:USDT | below_1h_threshold | +2.18% | +2.59% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
