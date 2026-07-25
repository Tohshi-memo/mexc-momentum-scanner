# Decision Report

- generated_at: 2026-07-25T09:46:22.841930+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9507**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9507, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.92% | **-0.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +1.43% | **+0.57%** |
| LIMIT_6PCT | 4/20 | 20.0% | +2.61% | **+0.52%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.04% | **+0.26%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.06% | **+0.05%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.15% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.30% | **+1.61%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.11% | **+1.16%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.12% | **+1.01%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +3.98% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 139件 (TP 46 / SL 88 / EXP 5)
- 最新: SYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$427.09** / 初期 $100.00 (+327.09%)
- 確定: 3337件 (Win 1052 / Loss 1081 / Flat 1204) / skip 2731件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EUL/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $427.09

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1165件 (Win 312 / Loss 254 / Flat 599) / skip 1753件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0503 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$105.96** / 初期 $100.00 (+5.96%)
- 確定: 554件 (Win 185 / Loss 213 / Flat 156) / pending 5件 / skip 420件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000371 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: EUL/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $105.96

## 6. Latest Market Context

- 更新: 2026-07-25T09:46:13.354273+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=63910.3
- Funnel: target 897 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.4 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DEXE/USDT:USDT | +103.06% | $86,637,085.95 |
| EUL/USDT:USDT | +70.76% | $4,665,256.16 |
| AKE/USDT:USDT | +24.25% | $49,565,146.26 |
| PROM/USDT:USDT | +22.46% | $3,722,906.26 |
| B2/USDT:USDT | +16.01% | $3,504,359.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PROM/USDT:USDT | below_1h_threshold | +3.85% | +3.75% |
| MORPHO/USDT:USDT | below_1h_threshold | +1.76% | +1.65% |
| VVV/USDT:USDT | below_1h_threshold | +1.73% | +1.62% |
| DOT/USDT:USDT | below_1h_threshold | +0.90% | +0.80% |
| APE/USDT:USDT | below_1h_threshold | +0.75% | +0.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
