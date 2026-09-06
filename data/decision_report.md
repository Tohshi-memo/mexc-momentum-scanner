# Decision Report

- generated_at: 2026-09-06T13:26:17.229952+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13817**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.33% / filled 20/20。**
- 全期間 MARKET基準: n=13817, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.33% | **+2.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.33% | **+2.33%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.86% | **+1.40%** |
| LIMIT_3PCT | 12/20 | 60.0% | +2.09% | **+1.25%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.22% | **+0.85%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.73% | **+0.78%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.22% | **+1.67%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.10% | **+0.33%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.74% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$839.16** / 初期 $100.00 (+739.16%)
- 確定: 5123件 (Win 1537 / Loss 1678 / Flat 1908) / skip 5255件
- 成長率目線: 平均log +0.000415 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COTI/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $839.16

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.52** / 初期 $100.00 (+90.52%)
- 確定: 2562件 (Win 716 / Loss 613 / Flat 1233) / skip 4666件
- 成長率目線: 平均log +0.000252 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0463 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $190.52

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.06** / 初期 $100.00 (+19.06%)
- 確定: 2428件 (Win 722 / Loss 926 / Flat 780) / pending 2件 / skip 2856件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000101 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $119.06

## 6. Latest Market Context

- 更新: 2026-09-06T13:26:05.500688+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=79774.2
- Funnel: target 1054 → liquid 125 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAY/USDT:USDT | +61.11% | $6,916,595.13 |
| ARB/USDT:USDT | +43.43% | $178,534,584.38 |
| FONE/USDT:USDT | +30.39% | $1,050,704.45 |
| FLOCK/USDT:USDT | +29.17% | $2,303,404.79 |
| COTI/USDT:USDT | +18.46% | $1,498,956.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZRO/USDT:USDT | below_1h_threshold | +1.83% | +1.96% |
| MAGMA/USDT:USDT | below_1h_threshold | +1.47% | +1.60% |
| NEAR/USDT:USDT | below_1h_threshold | +1.45% | +1.58% |
| ZEC/USDT:USDT | below_1h_threshold | +1.11% | +1.24% |
| TAO/USDT:USDT | below_1h_threshold | +0.78% | +0.92% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
