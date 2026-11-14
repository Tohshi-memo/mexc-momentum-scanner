# Decision Report

- generated_at: 2026-11-14T10:56:28.417274+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18891**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.66% / filled 20/20。**
- 全期間 MARKET基準: n=18891, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.66% | **+1.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.66% | **+1.66%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.49% | **+1.42%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.26% | **+1.01%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.41% | **+0.77%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.73% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +2.41% | **+0.96%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.40% | **+0.20%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.14% | **-0.07%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | -0.27% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$121.01** / 初期 $100.00 (+21.01%)
- 確定トレード: 275件 (TP 99 / SL 168 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.01
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,769.15** / 初期 $100.00 (+1669.15%)
- 確定: 7296件 (Win 2102 / Loss 2339 / Flat 2855) / skip 8156件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `MARKET` TP_HIT account +1.00% 残高後 $1,769.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$419.72** / 初期 $100.00 (+319.72%)
- 確定: 4899件 (Win 1312 / Loss 1080 / Flat 2507) / skip 7403件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0708 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_9PCT_LONG` TP_HIT account +0.69% 残高後 $419.72

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7050件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000232 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-14T10:56:12.129790+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=67270.0
- Funnel: target 1071 → liquid 143 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHELL/USDT:USDT | +39.19% | $4,796,045.29 |
| AKE/USDT:USDT | +25.73% | $85,776,728.28 |
| DODO/USDT:USDT | +23.72% | $1,537,564.27 |
| ARIA/USDT:USDT | +5.73% | $4,219,445.62 |
| NIGHT/USDT:USDT | +5.00% | $1,419,009.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DODO/USDT:USDT | below_1h_threshold | +2.89% | +3.06% |
| ARIA/USDT:USDT | below_1h_threshold | +2.28% | +2.45% |
| MUU/USDT:USDT | below_1h_threshold | +0.42% | +0.59% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +0.34% | +0.51% |
| STXSTOCK/USDT:USDT | below_1h_threshold | +0.33% | +0.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
