# Decision Report

- generated_at: 2026-07-22T17:26:24.234749+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9298**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.45% / filled 20/20。**
- 全期間 MARKET基準: n=9298, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 13/20 | 65.0% | +1.14% | **+0.74%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.93% | **+0.60%** |
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_BB3S | 4/17 | 23.5% | +1.25% | **+0.29%** |
| LIMIT_FIB1272 | 13/20 | 65.0% | +0.38% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.97% | **+0.68%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.51% | **+0.30%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +0.39% | **+0.12%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.06% | **+0.06%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.09% | **+0.05%** |

## 2. $100 Live Portfolio

- 残高: **$105.37** / 初期 $100.00 (+5.37%)
- 確定トレード: 133件 (TP 45 / SL 83 / EXP 5)
- 最新: DEXE/USDT:USDT SL_HIT PnL -4.00% 残高後 $105.37
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$431.91** / 初期 $100.00 (+331.91%)
- 確定: 3289件 (Win 1039 / Loss 1058 / Flat 1192) / skip 2570件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SNXX/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $431.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.82** / 初期 $100.00 (+30.82%)
- 確定: 1160件 (Win 312 / Loss 253 / Flat 595) / skip 1549件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0851 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $130.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.55** / 初期 $100.00 (+1.55%)
- 確定: 425件 (Win 142 / Loss 176 / Flat 107) / pending 3件 / skip 351件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000171 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $101.55

## 6. Latest Market Context

- 更新: 2026-07-22T17:26:17.246878+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.30% price=66000.4
- Funnel: target 890 → liquid 182 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DEXE/USDT:USDT | +7.11% | $13,849,673.07 |
| BANK/USDT:USDT | +6.91% | $91,556,574.43 |
| RIF/USDT:USDT | +5.25% | $3,898,010.18 |
| BROCCOLIF3B/USDT:USDT | +4.94% | $1,565,228.00 |
| WLD/USDT:USDT | +4.85% | $33,611,557.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +2.53% | +2.83% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +2.19% | +2.49% |
| PROM/USDT:USDT | below_1h_threshold | +2.14% | +2.44% |
| WLD/USDT:USDT | below_1h_threshold | +1.42% | +1.72% |
| ZAMA/USDT:USDT | below_1h_threshold | +1.26% | +1.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
