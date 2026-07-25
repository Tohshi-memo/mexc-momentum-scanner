# Decision Report

- generated_at: 2026-07-25T17:06:18.191756+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9534**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9534, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.09% | **-1.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/17 | 17.6% | +0.77% | **+0.14%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | -0.31% | **-0.06%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.31% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.94% | **+1.55%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.19% | **+1.42%** |
| MARKET_LONG | 20/20 | 100.0% | +0.87% | **+0.87%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.72% | **+0.77%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$448.55** / 初期 $100.00 (+348.55%)
- 確定: 3362件 (Win 1065 / Loss 1089 / Flat 1208) / skip 2733件
- 成長率目線: 平均log +0.000446 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $448.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.12** / 初期 $100.00 (+36.12%)
- 確定: 1187件 (Win 325 / Loss 259 / Flat 603) / skip 1758件
- 成長率目線: 平均log +0.000260 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1481 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $136.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$107.58** / 初期 $100.00 (+7.58%)
- 確定: 579件 (Win 195 / Loss 222 / Flat 162) / pending 6件 / skip 422件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000512 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $107.58

## 6. Latest Market Context

- 更新: 2026-07-25T17:06:11.429439+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=64206.2
- Funnel: target 898 → liquid 134 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +15.64% | $89,350,070.61 |
| ESPORTS/USDT:USDT | +11.33% | $21,824,911.75 |
| DEXE/USDT:USDT | +6.47% | $131,482,629.09 |
| ZAMA/USDT:USDT | +4.91% | $6,598,935.91 |
| SHIB/USDT:USDT | +4.37% | $12,619,757.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SHIB/USDT:USDT | below_1h_threshold | +2.27% | +2.23% |
| EUL/USDT:USDT | below_1h_threshold | +1.48% | +1.44% |
| FLOKI/USDT:USDT | below_1h_threshold | +1.19% | +1.15% |
| PEPE/USDT:USDT | below_1h_threshold | +0.94% | +0.90% |
| SNXX/USDT:USDT | below_1h_threshold | +0.91% | +0.87% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
