# Decision Report

- generated_at: 2026-07-11T13:56:05.444687+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8536**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.03% / filled 20/20。**
- 全期間 MARKET基準: n=8536, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.03% | **+2.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.03% | **+2.03%** |
| ASK | 15/15 | 100.0% | +1.74% | **+1.74%** |
| LIMIT_2PCT | 15/20 | 75.0% | +2.10% | **+1.57%** |
| LIMIT_3PCT | 12/20 | 60.0% | +2.19% | **+1.32%** |
| LIMIT_ATR | 12/20 | 60.0% | +2.06% | **+1.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.13% | **+0.53%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | -1.14% | **-0.40%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | -1.11% | **-0.61%** |
| MARKET_LONG | 20/20 | 100.0% | -0.61% | **-0.61%** |

## 2. $100 Live Portfolio

- 残高: **$104.09** / 初期 $100.00 (+4.09%)
- 確定トレード: 83件 (TP 30 / SL 52 / EXP 1)
- 最新: NES/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.09
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$316.35** / 初期 $100.00 (+216.35%)
- 確定: 2724件 (Win 861 / Loss 915 / Flat 948) / skip 2373件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: T/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $316.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 642件 (Win 152 / Loss 159 / Flat 331) / skip 1305件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.48** / 初期 $100.00 (-0.52%)
- 確定: 3件 (Win 0 / Loss 3 / Flat 0) / pending 2件 / skip 0件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000253 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: T/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.48

## 6. Latest Market Context

- 更新: 2026-07-11T13:55:59.446219+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=64233.5
- Funnel: target 863 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| T/USDT:USDT | +27.08% | $3,308,949.82 |
| CLO/USDT:USDT | +24.70% | $1,100,523.72 |
| BEAT/USDT:USDT | +20.37% | $35,892,106.91 |
| VIRTUAL/USDT:USDT | +15.13% | $37,140,367.36 |
| ANSEM/USDT:USDT | +13.99% | $7,340,575.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| THETA/USDT:USDT | below_1h_threshold | +2.78% | +2.68% |
| ARB/USDT:USDT | below_1h_threshold | +2.35% | +2.25% |
| ETHFI/USDT:USDT | below_1h_threshold | +2.26% | +2.16% |
| UNI/USDT:USDT | below_1h_threshold | +2.20% | +2.10% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +1.88% | +1.78% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
