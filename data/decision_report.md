# Decision Report

- generated_at: 2026-11-14T10:16:22.966938+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18888**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.26% / filled 20/20。**
- 全期間 MARKET基準: n=18888, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.26% | **+2.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.26% | **+2.26%** |
| LIMIT_1PCT | 19/20 | 95.0% | +2.07% | **+1.96%** |
| LIMIT_2PCT | 16/20 | 80.0% | +2.01% | **+1.61%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.58% | **+1.11%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.30% | **+0.65%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +1.61% | **+0.56%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | -0.44% | **-0.16%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | -0.31% | **-0.19%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | -0.36% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.01** / 初期 $100.00 (+21.01%)
- 確定トレード: 275件 (TP 99 / SL 168 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.01
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,769.28** / 初期 $100.00 (+1669.28%)
- 確定: 7293件 (Win 2101 / Loss 2337 / Flat 2855) / skip 8156件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOPH/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $1,769.28

## 4. Robust Adaptive DryRun ($100)

- 残高: **$416.85** / 初期 $100.00 (+316.85%)
- 確定: 4896件 (Win 1311 / Loss 1080 / Flat 2505) / skip 7403件
- 成長率目線: 平均log +0.000292 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0687 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOPH/USDT:USDT `LIMIT_9PCT_LONG` TP_HIT account +0.69% 残高後 $416.85

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7046件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000232 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-14T10:16:09.437481+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.26% price=67207.6
- Funnel: target 1071 → liquid 142 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHELL/USDT:USDT | +40.19% | $4,638,743.48 |
| AKE/USDT:USDT | +30.86% | $82,525,139.22 |
| DODO/USDT:USDT | +22.25% | $1,474,035.43 |
| NIGHT/USDT:USDT | +6.46% | $1,360,654.91 |
| PIEVERSE/USDT:USDT | +5.67% | $1,030,335.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +4.13% | +4.39% |
| DODO/USDT:USDT | below_1h_threshold | +1.73% | +1.99% |
| SOPH/USDT:USDT | below_1h_threshold | +1.43% | +1.69% |
| BERA/USDT:USDT | below_1h_threshold | +1.22% | +1.47% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +0.88% | +1.13% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
