# Decision Report

- generated_at: 2026-07-25T14:56:20.424202+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9521**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9521, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 7/20 | 35.0% | +3.13% | **+1.10%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.06% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.41% | **+1.13%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.14% | **+0.97%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.36% | **+0.88%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$440.68** / 初期 $100.00 (+340.68%)
- 確定: 3349件 (Win 1059 / Loss 1085 / Flat 1205) / skip 2733件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $440.68

## 4. Robust Adaptive DryRun ($100)

- 残高: **$134.07** / 初期 $100.00 (+34.07%)
- 確定: 1175件 (Win 319 / Loss 256 / Flat 600) / skip 1757件
- 成長率目線: 平均log +0.000250 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1658 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $134.07

## 5. Causal Adaptive DryRun ($100)

- 残高: **$107.51** / 初期 $100.00 (+7.51%)
- 確定: 568件 (Win 193 / Loss 218 / Flat 157) / pending 5件 / skip 420件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000581 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $107.51

## 6. Latest Market Context

- 更新: 2026-07-25T14:56:10.605447+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=64184.0
- Funnel: target 898 → liquid 143 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.0 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DEXE/USDT:USDT | +66.33% | $125,666,140.40 |
| EUL/USDT:USDT | +59.94% | $11,646,903.93 |
| AKE/USDT:USDT | +33.69% | $46,831,450.28 |
| PROM/USDT:USDT | +17.32% | $4,977,553.11 |
| BANK/USDT:USDT | +15.53% | $75,850,183.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +4.01% | +3.94% |
| BANK/USDT:USDT | below_1h_threshold | +3.42% | +3.34% |
| SHIB/USDT:USDT | below_1h_threshold | +2.84% | +2.77% |
| AVAX/USDT:USDT | below_1h_threshold | +1.58% | +1.50% |
| VVV/USDT:USDT | below_1h_threshold | +1.44% | +1.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
