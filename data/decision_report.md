# Decision Report

- generated_at: 2026-11-12T07:56:32.829938+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18724**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.66% / filled 20/20。**
- 全期間 MARKET基準: n=18724, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.87% | **+0.87%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.93% | **+0.84%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.12% | **+0.12%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.05% | **+0.03%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | -0.04% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 273件 (TP 99 / SL 166 / EXP 8)
- 最新: IDOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,706.89** / 初期 $100.00 (+1606.89%)
- 確定: 7234件 (Win 2083 / Loss 2317 / Flat 2834) / skip 8051件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KGEN/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.09% 残高後 $1,706.89

## 4. Robust Adaptive DryRun ($100)

- 残高: **$389.99** / 初期 $100.00 (+289.99%)
- 確定: 4780件 (Win 1283 / Loss 1058 / Flat 2439) / skip 7355件
- 成長率目線: 平均log +0.000285 / 幾何平均 +0.028% per trade / maxDD +4.29%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0272 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KGEN/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.08% 残高後 $389.99

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6882件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000199 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-12T07:56:14.279154+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=73609.7
- Funnel: target 1103 → liquid 146 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KGEN/USDT:USDT | +22.27% | $2,516,668.96 |
| SOXS/USDT:USDT | +10.00% | $66,392,369.81 |
| Q/USDT:USDT | +5.61% | $4,770,482.09 |
| SQQQ/USDT:USDT | +3.87% | $2,172,287.74 |
| AMDSTOCK/USDT:USDT | +1.95% | $23,387,794.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIN/USDT:USDT | below_1h_threshold | +2.80% | +2.64% |
| GRAM/USDT:USDT | below_1h_threshold | +2.46% | +2.30% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +1.04% | +0.88% |
| UKOIL/USDT:USDT | below_1h_threshold | +1.00% | +0.84% |
| USOIL/USDT:USDT | below_1h_threshold | +0.94% | +0.79% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
