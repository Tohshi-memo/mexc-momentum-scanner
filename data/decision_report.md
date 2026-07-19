# Decision Report

- generated_at: 2026-07-19T16:26:09.417038+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9055**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.98% / filled 20/20。**
- 全期間 MARKET基準: n=9055, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.98% | **+1.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.98% | **+1.98%** |
| LIMIT_2PCT | 15/20 | 75.0% | +2.42% | **+1.82%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.52% | **+0.70%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.83% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +3.59% | **+1.25%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +2.23% | **+1.23%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.00% | **+0.00%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.44% | **-0.24%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$397.29** / 初期 $100.00 (+297.29%)
- 確定: 3117件 (Win 978 / Loss 997 / Flat 1142) / skip 2499件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TLM/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $397.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$125.90** / 初期 $100.00 (+25.90%)
- 確定: 1016件 (Win 263 / Loss 217 / Flat 536) / skip 1450件
- 成長率目線: 平均log +0.000227 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0574 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TLM/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $125.90

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.65** / 初期 $100.00 (+0.65%)
- 確定: 255件 (Win 87 / Loss 128 / Flat 40) / pending 3件 / skip 267件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000282 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TLM/USDT:USDT `MARKET_LONG` TP_HIT account +0.34% 残高後 $100.65

## 6. Latest Market Context

- 更新: 2026-07-19T16:26:04.633547+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=64580.6
- Funnel: target 885 → liquid 128 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.8 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TLM/USDT:USDT | +13.79% | $11,368,224.88 |
| VANRY/USDT:USDT | +4.02% | $1,030,707.59 |
| SYN/USDT:USDT | +2.82% | $3,479,476.02 |
| SLX/USDT:USDT | +2.45% | $1,125,075.14 |
| AKE/USDT:USDT | +1.62% | $48,837,073.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VANRY/USDT:USDT | below_1h_threshold | +4.03% | +3.97% |
| SYN/USDT:USDT | below_1h_threshold | +2.83% | +2.77% |
| SLX/USDT:USDT | below_1h_threshold | +2.08% | +2.02% |
| B/USDT:USDT | below_1h_threshold | +1.67% | +1.61% |
| AKE/USDT:USDT | below_1h_threshold | +1.63% | +1.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
