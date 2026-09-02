# Decision Report

- generated_at: 2026-09-02T06:06:31.870795+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13310**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13310, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.23% | **-0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 12/20 | 60.0% | +2.36% | **+1.42%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +3.17% | **+0.95%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.95% | **+0.81%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +5.16% | **+1.55%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.39% | **+1.19%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.40% | **+0.84%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.52% | **+0.68%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.83% | **+0.54%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 197件 (TP 73 / SL 119 / EXP 5)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$824.64** / 初期 $100.00 (+724.64%)
- 確定: 4939件 (Win 1502 / Loss 1625 / Flat 1812) / skip 4932件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $824.64

## 4. Robust Adaptive DryRun ($100)

- 残高: **$175.16** / 初期 $100.00 (+75.16%)
- 確定: 2289件 (Win 636 / Loss 548 / Flat 1105) / skip 4432件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1150 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $175.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.88** / 初期 $100.00 (+14.88%)
- 確定: 2089件 (Win 610 / Loss 817 / Flat 662) / pending 0件 / skip 2693件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000397 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FILECOIN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.88

## 6. Latest Market Context

- 更新: 2026-09-02T06:06:20.424779+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=77661.0
- Funnel: target 1041 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FONE/USDT:USDT | +40.81% | $1,512,639.36 |
| MAGMA/USDT:USDT | +34.46% | $5,668,495.46 |
| CASHCAT/USDT:USDT | +26.07% | $1,459,344.10 |
| UAI/USDT:USDT | +20.16% | $20,717,139.10 |
| BONER/USDT:USDT | +18.33% | $2,622,299.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACE/USDT:USDT | below_1h_threshold | +2.45% | +2.39% |
| USELESS/USDT:USDT | below_1h_threshold | +1.08% | +1.03% |
| AAVE/USDT:USDT | below_1h_threshold | +0.79% | +0.73% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.72% | +0.67% |
| CHIP/USDT:USDT | below_1h_threshold | +0.69% | +0.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
