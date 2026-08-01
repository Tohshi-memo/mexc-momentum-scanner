# Decision Report

- generated_at: 2026-08-01T03:31:21.589112+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10054**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.73% / filled 20/20。**
- 全期間 MARKET基準: n=10054, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.73% | **+1.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.73% | **+1.73%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.61% | **+1.28%** |
| LIMIT_ATR | 7/20 | 35.0% | +1.34% | **+0.47%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.45% | **+0.45%** |
| LIMIT_3PCT | 11/20 | 55.0% | +0.65% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.45% | **+0.27%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | -0.29% | **-0.12%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | -0.28% | **-0.13%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$563.34** / 初期 $100.00 (+463.34%)
- 確定: 3606件 (Win 1150 / Loss 1180 / Flat 1276) / skip 3009件
- 成長率目線: 平均log +0.000479 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KOMA/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $563.34

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2186件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0295 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$112.28** / 初期 $100.00 (+12.28%)
- 確定: 873件 (Win 283 / Loss 344 / Flat 246) / pending 6件 / skip 651件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000222 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $112.28

## 6. Latest Market Context

- 更新: 2026-08-01T03:31:15.185874+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=63000.0
- Funnel: target 921 → liquid 168 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.8 >= 65=1, 4h RSI 65.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +35.39% | $1,209,073.36 |
| KOMA/USDT:USDT | +31.53% | $18,303,317.79 |
| BTW/USDT:USDT | +22.12% | $2,593,533.22 |
| GIGGLE/USDT:USDT | +16.71% | $23,815,118.40 |
| TLM/USDT:USDT | +15.67% | $1,860,376.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGGLE/USDT:USDT | below_1h_threshold | +4.47% | +4.53% |
| TAG/USDT:USDT | below_1h_threshold | +3.13% | +3.20% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.73% | +1.79% |
| UB/USDT:USDT | below_1h_threshold | +1.71% | +1.77% |
| FLOW/USDT:USDT | below_1h_threshold | +1.33% | +1.39% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
