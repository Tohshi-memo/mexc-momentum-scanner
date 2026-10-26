# Decision Report

- generated_at: 2026-10-26T09:51:16.971169+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17469**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.44% / filled 20/20。**
- 全期間 MARKET基準: n=17469, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.44% | **+2.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.44% | **+2.44%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.83% | **+1.55%** |
| LIMIT_ATR | 8/20 | 40.0% | +3.51% | **+1.40%** |
| LIMIT_8PCT | 4/20 | 20.0% | +5.85% | **+1.17%** |
| LIMIT_BB3S | 3/16 | 18.8% | +5.27% | **+0.99%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.11% | **+1.02%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +1.36% | **+0.47%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.25% | **+0.22%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +0.21% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 251件 (TP 93 / SL 150 / EXP 8)
- 最新: CT/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,534.60** / 初期 $100.00 (+1434.60%)
- 確定: 6719件 (Win 1956 / Loss 2151 / Flat 2612) / skip 7311件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,534.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$315.90** / 初期 $100.00 (+215.90%)
- 確定: 4012件 (Win 1112 / Loss 950 / Flat 1950) / skip 6868件
- 成長率目線: 平均log +0.000287 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0546 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DOOD/USDT:USDT `LIMIT_9PCT_LONG` TP_HIT account +0.69% 残高後 $315.90

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5627件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000172 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-26T09:51:04.458074+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.39% price=80518.0
- Funnel: target 1073 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOOD/USDT:USDT | +57.16% | $2,015,710.64 |
| BULLA/USDT:USDT | +35.93% | $1,142,144.35 |
| KIMCHI/USDT:USDT | +31.38% | $3,377,702.48 |
| QNT/USDT:USDT | +10.91% | $68,680,597.32 |
| DODO/USDT:USDT | +9.58% | $1,421,308.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BULLA/USDT:USDT | below_relative_strength | +5.37% | +4.97% |
| QNT/USDT:USDT | below_1h_threshold | +4.50% | +4.11% |
| CHIP/USDT:USDT | below_1h_threshold | +2.74% | +2.34% |
| SNXX/USDT:USDT | below_1h_threshold | +1.98% | +1.59% |
| BEAT/USDT:USDT | below_1h_threshold | +1.96% | +1.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
